import requests,datetime
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request

app = Flask(__name__)


def fetch_table_data(year):
    url = f'https://www.sii.cl/valores_y_fechas/uf/uf{year}.htm'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'id': 'table_export'})
    rows = table.find_all('tr')

    # List of month names as they appear in the table header
    data = []
    for i in range(1, len(rows)):
        row = rows[i]
        day = int(row.find('th').text.strip())
        columns = row.find_all('td')

        month_values = [
            float(value.text.strip().replace('.', '').replace(',', '.'))
            for value in columns if value.text.strip() != ''
        ]
        # Convert the month names to numbers
        month_numbers = [i+1 for i in range(len(month_values))]
        month_data = {month_numbers[index]: value for index, value in enumerate(month_values)}
        print(month_data)
        data.append((day, month_data))
    return data

@app.route("/api/uf", methods=["GET"])
def get_value():
    date = request.args.get("date")
    if not date:
        return jsonify({"error": "Missing date parameter"}), 400

    year = date.split("-")[0]
    table_data = fetch_table_data(year)

    # Convert the requested date to the same format as the dates in the table_data list
    requested_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    requested_day = requested_date.day
    requested_month = requested_date.month

    for item in table_data:
        day = item[0]
        month_data = item[1]

        # Check if the requested date matches the date in the table_data list
        if day == requested_day and requested_month in month_data:
            # Convert the UF value to a dictionary with YYYY-MM-DD format
            uf_value = {date: month_data[requested_month]}
            return jsonify(uf_value), 200

    return jsonify({"error": "Date not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
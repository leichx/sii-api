# UF API

This project provides an API to get the value of the UF (Unidad de Fomento) for a specific date.

## Getting started

To run this project, you'll need to have Python 3 installed on your machine.

1. Clone this repository to your local machine
2. Open a terminal and navigate to the project directory
3. Run `pip install -r requirements.txt` to install the project dependencies
4. Run `python app.py` to start the server
5. The server will be available at http://localhost:5000

## Endpoints

### `/api/uf`

This endpoint returns the value of the UF for a specific date.

#### Parameters

- `date` (required) - The date for which to get the UF value. The date must be in the format `YYYY-MM-DD`.

#### Example

Request:

`GET /api/uf?date=2022-04-18`


Response:

`
{
"2022-04-18": 29153.43
}
`
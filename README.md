# timberinvoice

Timberinvoice is a web-based  solution for managing clients and invoices. Here is a demo of the application (running with a Vue.js frontend) - https://friendly-pare-762c4d.netlify.com/

## Synopsis

Timberinvoice runs Python web service running on Django Rest Framework (DRF), Nginx and deployed on a Docker container registry on Heroku. It was built using a micro-service based architecture.

## API Endpoints

Here are the API Endpoints and needed payloads that could be used to create requests from any frontend client (Vue.js, React.js, Angular.js etc)

### Register [POST]

`/api/register/`



`{
	"username": "name",
	"email": "name@mail.com",
	"first_name": "Name",
	"last_name": "Surname ",
	"password": "yourpasswordhere",
	"company_name": "You, Inc",
	"office_address": "123, Stan Road",
	"office_telephone": 344567890
}`

### Login [POST]

`/api/login/`



`{
	"email": "name@email.com",
	"password": "yourpasswordhere"
}`

### Client [POST, GET, DELETE]

`/api/client/`



`{
	"company_name": "Dev Inc",
	"phone_number": 3444566664,
	"about": "some words",
	"address": "ABC Road",
	"city": "client city",
	"state": "client state",
	"country": "client country",
	"zipcode": "877"
}`

### Invoice [POST, GET, DELETE, PUT]

`/api/invoice/`



`{
	"invoice_id": "1x1887yy",
	"due_date": "2020-04-04",
	"payment_term": "End of Year",
	"shipping_address": "J123, ABC road",
	"vat": 6,
	"dispatch_personnel": "your name"
}`

## Motivation

This project is for test purposes 

## Installation

Local Installation:
`-- git clone https://github.com/luckyadogun/timberinvoice.git`

`-- cd timberinvoice`

`-- setup Postgres DB`

`-- run python manage.py migrate`

`-- python manage.py runserver`

Cloud Installation:
-- install Docker [https://docs.docker.com/get-started/]

`-- docker pull tobore/timberr:latest`

`-- docker run tobore/timberr`

## Tests

Navigate to the project root and run

`-- python manage.py tests`

## Contributors

This project is made for test purposes but can be forked

## License

MIT

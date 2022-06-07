import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('productId')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('productId')

    if name:
        if name == '75542e38-563f-436f-adeb-f426f1dabb5c':
            return func.HttpResponse(f"Alo teste outr avez{name} is Starfruit Explosion and the description is This starfruit ice cream is out of this world!")
        else:
            return func.HttpResponse(f"The product not found")
    else:
        return func.HttpResponse(
             "Product ID not found",
             status_code=200
        )

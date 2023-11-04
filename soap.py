import yaml
from zeep import Client, Settings

with open('config.yaml', encoding='utf-8') as f:
    config = yaml.safe_load(f)

settings = Settings(strict=False)
client = Client(wsdl=config["soap_wsdl_url"], settings=settings)


def check_text(word):
    return client.service.checkText(word)


if __name__ == '__main__':
    print(check_text('малако'))

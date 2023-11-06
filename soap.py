import yaml
import logging
from zeep import Client, Settings

with open('config.yaml', encoding='utf-8') as f:
    config = yaml.safe_load(f)

settings = Settings(strict=False)
client = Client(wsdl=config["soap_wsdl_url"], settings=settings)


def get_correction_variants(word):
    logging.debug(f"Get correction variants for \"{word}\".")
    try:
        response = client.service.checkText(word)
        if not response:
            logging.error(f"Text not contains errors.")
            return []
    except:
        logging.exception(f"Exception while check text \"{word}\".")
        return []
    return response[0]["s"]


if __name__ == '__main__':
    print(get_correction_variants('шляпаc'))

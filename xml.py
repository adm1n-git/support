
from support.logger import logger;
import xmltodict, os;

def from_xml(path="", str=""):
    if path:
        if os.path.exists(path):
            with open(path, "r") as file:
                return xmltodict.parse(file.read());
        else:
            logger.error(f"Path {path} doesn't exist.");
    else:
        return xmltodict.parse(str);

def to_xml(path="", object=dict()):
    if path:
        with open(path, "w") as file:
            file.write(xmltodict.unparse(object));
    else:
        return xmltodict.unparse(object);

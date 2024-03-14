import faceIdIdentifier

# create environment via: python3.11 -m venv venv
# activate environment via: source venv/bin/activate
# install packages via: pip install -r requirements.txt
# upgrade pip via: pip install --upgrade pip
# run program via: python main.py

# total setup: python3.11 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && pip install --upgrade pip && clear && python main.py;


if __name__ == "__main__":
    print("\n\nNumber 1.")
    identifier = faceIdIdentifier.faceIdIdentifier("images/mr_bean.jpg", "images/mr_bean_id.jpg")
    identifier.evaluate()
    
    print("\n\nNumber 2.")
    identifier = faceIdIdentifier.faceIdIdentifier("images/pee_wee.jpg", "images/mr_bean_id.jpg")
    identifier.evaluate()
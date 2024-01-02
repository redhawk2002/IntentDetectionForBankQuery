# Bank System Setup Instructions

## 1. Download the Model

- **Link:** [uncased_L-12_H-768_A-12.zip](https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-12_H-768_A-12.zip)

## 2. Unzip the Downloaded File

Extract the contents of the downloaded ZIP file.

## 3. Create the "model" Folder

1. Create a new folder named `model` within the `ModelServer` folder.
2. Move the unzipped files into the `model` folder.

## 4. Run the Model Training

Execute the `modelTrainingandSave.ipynb` file.

## 5. Run the Flask App

In your terminal, run the following command:

```bash
python -m flask --app .\app.py run
```
## 6. Run the Node.js Server
In your terminal, run the following command:
npm run dev


## 7. Open the Index File

Open the `index.html` file in your web browser to access the Bank System.

**The Bank System is now ready to be used!**

## Demo

**See a live demonstration of the system in action:**


https://github.com/redhawk2002/IntentDetectionForBankQuery/assets/77795912/35c1b50b-5366-4ef5-8e0c-465281e09580


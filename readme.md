Bank System Setup Instructions:

1. Download the Model:
   - **Link:** [uncased_L-12_H-768_A-12.zip](https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-12_H-768_A-12.zip)

2. Unzip the downloaded file.

3. Create a folder named "model" inside the "ModelServer" folder. Move the unzipped files to the "model" folder.

4. Run the file `modelTrainingandSave.ipynb`.

5. Run the file `app.py` by executing the following command in the terminal: `python -m flask --app .\app.py run`

6. Run the file `server.js` by executing the following command in the terminal: `npm run dev`

7. Open the index file in your browser.

The Bank System is now ready to be used.

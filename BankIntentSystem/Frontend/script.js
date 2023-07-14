const clickToRecord = document.getElementById("click_to_record");

clickToRecord.addEventListener("click", function () {
  const speech = true;
  window.SpeechRecognition = window.webkitSpeechRecognition;

  const recognition = new SpeechRecognition();
  recognition.interimResults = true;

  let finalTranscript = ""; // Store the final transcript

  recognition.addEventListener("result", (e) => {
    const transcript = Array.from(e.results)
      .map((result) => result[0])
      .map((result) => result.transcript)
      .join("");

    if (e.results[e.results.length - 1].isFinal) {
      finalTranscript = transcript;
      console.log("Final transcript:", finalTranscript);

      // Make a POST request to the server with the final transcript
      if (speech == true) {
        axios
          .post("http://localhost:4000/getText", { text: finalTranscript })
          .then((response) => {
            console.log(response.data);
          })
          .catch((error) => {
            console.error(error);
          });
      }
    }

    document.getElementById("convert_text").innerHTML = transcript;
    console.log("Current transcript:", transcript);
  });
  if (speech == true) {
    recognition.start();
  }
});

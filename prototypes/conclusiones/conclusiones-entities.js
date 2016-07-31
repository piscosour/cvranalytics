// for element in the database
//	get element
//	get element text
//	build entity request
//	build http request with api credentials
//	append entities to element
//	push to db

var nl_access_token = "ya29.CjAvA0266t5nqrT2nxklu3oFnSRzHCLX5LiMDpglgbJaGGirua7qLQotTN-xW0wiW9U";

function getConclusion(conclusionId) {
	var conclusion_text = firebase.database().ref('/conclusiones/' + conclusionId).once('value').then(function(snapshot) {
		if (snapshot.val()) {
			contenido = snapshot.val().contenido;
			console.log("Success: fetch " + conclusionId);
			
			var entities = buildRequest(contenido, nl_access_token, conclusionId);
		}
	});
};

function buildRequest(data_text, token, conclusionId) {
	var request = new XMLHttpRequest();
	request.open('POST', 'https://language.googleapis.com/v1beta1/documents:analyzeEntities', false);
	request.setRequestHeader('Content-type','application/json');
	request.setRequestHeader('Authorization', 'Bearer ' + token);

	var data = '{ "document": { "type": "PLAIN_TEXT", "content": "' + data_text + '" }, "encodingType": "UTF8" }';
	var response;

	request.send(data);

    if (request.readyState == 4 && request.status == 200) {
        var response = JSON.parse(request.responseText);
        console.log(response);

        firebase.database().ref('/conclusiones/' + conclusionId).update({
			entities: response.entities,
			language: response.language
		});
	};
};

function requestFactory() {
	for (i = 1; i < 172; i++) {
		getConclusion(i);
	};
};

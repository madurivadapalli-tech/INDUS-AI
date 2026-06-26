function askAI(){

    let query=document.getElementById("query").value;

    if(query===""){

        alert("Please enter your question.");

        return;

    }

    fetch("http://127.0.0.1:8000/chat?query="+encodeURIComponent(query))

    .then(response=>response.json())

    .then(data=>{

        document.getElementById("response").innerHTML=

        "<h3>AI Response</h3><p>"+data.Response+"</p>";

    })

    .catch(error=>{

        document.getElementById("response").innerHTML=

        "Unable to connect to backend.";

    });

}

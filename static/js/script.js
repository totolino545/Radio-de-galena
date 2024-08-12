const toastTrigger = document.getElementById('liveToastBtn');
const toastLiveExample = document.getElementById('liveToast');
let music = document.getElementById("music");
let artwork = document.getElementsByClassName("artwork")[0]; 
const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
let inputLista = document.getElementById('lista');
let inputLimit = document.getElementById('estaciones');
let urlRadio


if (toastTrigger) {  
  toastTrigger.addEventListener('click', () => {
    console.log(urlRadio);
    
    toastBootstrap.show()
    leerMetadatos(urlRadio)
  })
}
function borrarInput (){
  inputLista.value = "";
  inputLista.focus();
}
function borrarLimit (){
  inputLimit.value = "";
  inputLimit.focus();
}

function leerMetadatos(url) {
  fetch(`/reproduciendo?url=${url}`)
                .then(response => {
        if (!response.ok) {
            throw new Error('Error en la solicitud');
        }
        return response.json();  // Parsear la respuesta como JSON
        })
        .then(metadato => { 
            let [artista, titulo] = metadato.split(" - ", 2);  
            console.log("Artista:", artista);
            console.log("Título:", titulo)                           
            document.getElementById('interprete').innerHTML = artista;
            document.getElementById('titulo').innerHTML = titulo;
            return
        })
        .catch(error => {
            console.error('Error al cargar el metadato:', error);
        });
}

function reproducirAudio(url, favicon, name, country, bitrate, codec){
  toastBootstrap.show();
  document.getElementById("radio").innerHTML = name;
  document.getElementById("country").innerHTML = country;
  document.getElementById("titulo").innerHTML = name;
  document.getElementById("bitrate").innerHTML = bitrate;
  document.getElementById("codec").innerHTML = codec;
  urlRadio = url;
  leerMetadatos(url);
  artwork.setAttribute("style", "background:url(/static/img/disco.png), url('"+favicon+"') center no-repeat;");
  music.innerHTML = '<source src="'+url+'" type="audio/mp3">';
  music.load();
  music.addEventListener('playing', function() {
    document.getElementById("reproduciendo").innerHTML = "Playing";
  });
  music.addEventListener('pause', function() {
    document.getElementById("reproduciendo").innerHTML = "Stoped";
  }); 
  music.addEventListener('error', function() {
    console.error('Error al cargar el audio.');
  });
}





    

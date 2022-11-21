var activar=0;
function mostraMenu() {
  
  if (activar == 0) {
    document.getElementById("id_nav").classList.add("activar");
    document.getElementById("id_nav").classList.remove("desactivar");

    document.getElementById("id_logo").classList.add("activar");
    document.getElementById("id_logo").classList.remove("desactivar");

    activar = 1;
  } else {

    document.getElementById("id_logo").classList.remove("activar");
    document.getElementById("id_logo").classList.add("desactivar");

    document.getElementById("id_nav").classList.add("desactivar");
    document.getElementById("id_nav").classList.remove("activar");
    activar = 0;
  }
  
}

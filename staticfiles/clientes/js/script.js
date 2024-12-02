const header = document.querySelector("header");

window.addEventListener("scroll", function (){
    header.classList.toggle("sticky", window.scrollY > 60)
})


// Agregar un evento clic al elemento de clase .btn
/*
document.querySelector('.btn').addEventListener("click", function(){
    alert('¡Tu pedido ha sido registrado!');
})


// Agregar un evento clic a cada uno de los elementos encontrados de clase .btn
document.querySelectorAll('.btn').forEach(function(button){
    button.addEventListener('click', function(){
        alert('¡Tu pedido ha sido registrado!');
    })
})
*/

// Funcion para el botón 'pedido'
document.getElementById('btn-pedido').addEventListener('click', function(){
    alert("El pedido 93485793 ha sido generado")
})

document.getElementById('btn-promocion').addEventListener('click', function(){
    alert("Excelente decisión. ")
})


document.querySelectorAll('.navbar a[href^="#"]').forEach(function(enlace){
    enlace.addEventListener('click', function(e){
        e.preventDefault();
        // Desplazamiento suave
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        })
    })
})

// Cambiar las imágenes de fondo de la sección home

const imagenes = [
    'img/fondo-burguer.jpg',
    'img/boneless.jpg',
    'img/combos.jpg',
    'img/especiales.jpg',
    'img/hamburguesas.jpg',
];

const homeSection = document.querySelector('.home');
const intervalo = 10000; // 4000 ms = 4s

let indiceImagen = 0;

function cambiarFondo(){
    homeSection.style.backgroundImage = `linear-gradient(to left, rgba(211, 103, 103, 0.6), rgba(190,190,48, 0.3)) , url(${imagenes[indiceImagen]})`;
    indiceImagen = (indiceImagen + 1) % imagenes.length;  
    
}

setInterval(cambiarFondo, intervalo)


// Menú para pantallas pequeñas
let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');
let enlaces = document.querySelectorAll('.navbar a');

menu.onclick = () => {
    navbar.classList.toggle('open')
    menu.classList.toggle('bx-x')
}

enlaces.forEach(link => {
    link.onclick = () => {
        navbar.classList.remove('open')
        menu.classList.remove('bx-x')
    }
})


var typed = new Typed('#typed', {
    strings: ['La especial de la casa', 'Sabor para alegrar tus días', 'Abrimos todos los días'],
    typeSpeed: 40, 
    loop: "true",
    backSpeed: 20, 
});





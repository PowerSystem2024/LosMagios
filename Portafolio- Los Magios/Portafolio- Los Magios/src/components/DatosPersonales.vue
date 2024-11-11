<script setup>
import linkedin from '/src/assets/linkedin_icon.svg';
import instagram from '/src/assets/instagram_icon.svg';
import github from '/src/assets/github_icon.svg';

const title = 'Los Magios';
const descripcion = 'Somos un equipo de Desarrolladores en vías de Capacitación';
const residencia = 'Mendoza, Salta, Tucumán, Argentina';
const presentacion = 'Hola, Bienvenido al portafolio de Los Magios, somos un equipo que esta en constante aprendizaje y crecimiento gracias a la perseverancia de nuestros integrantes';
const redesSociales = [
  { id: 1, name: 'linkedin', src: linkedin, url: 'https://www.linkedin.com/in/pabloaparicio7/' },
  { id: 2, name: 'instagram', src: instagram, url: 'https://www.instagram.com/pabloaparicio7/' },
  { id: 3, name: 'github', src: github, url: 'https://github.com/PowerSystem2024/LosMagios' },
];


</script>

<template>
<section class="datos-personales">
  <div class="card">
    <h1>{{ title }}</h1>
    <h2>{{ descripcion }}</h2>
    <p>{{ presentacion }}</p>
    <ul class="container-lista">
      <li v-for="red in redesSociales" :key="red.id">
        <a :href="red.url"><img class="icon-redsocial" :src="red.src" width="35rem" :alt="red.name"></a>
      </li>
    </ul>
    <h4>{{ residencia }}</h4>
  </div>
</section>
</template>

<style scoped>
h1 {
  font-size: 2.5rem;
}

p {
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.card {
  background-color: rgb(255, 196, 0);
  border-radius: 10px;
  padding: 10px;
  margin: 10px;
  text-align: center;
}

.container-lista {
  display: flex;
  justify-content: center;
  list-style: none;
  padding: 0;
  margin: 0;
  text-align: center;
}

.icon-redsocial {
  align-items: center;
  background-color: rgb(129, 40, 13);
  border-radius: 50%;
  padding: 2px;
  margin: 5px;
  box-shadow: 0 0 5px rgba(109, 18, 18, 0.934);
}

.icon-redsocial:hover {
  background-color: rgb(107, 21, 21);
  box-shadow: 0 0 5px rgba(110, 29, 29, 0.934);
}

h3 {
  font-size: 1.2rem;
  font-weight: 600;
}
</style>

<script setup>
  import {ref} from 'vue';
  const fechaColor=ref([]);
  fechaColor.value=[
   {color:'#6e1111'},
   {color:'#6e1111'},
   {color:'#6e1111'},
   {color:'#6e1111'},
   {color:'#6e1111'},
];

  const educacion = ref([]);
  educacion.value = [
    { fecha: 'Pablo Aparicio', title: 'Quality Assuranca Analyst', descripcion: 'La Calidad NO se negocia.' },
    { fecha: 'Gonzalo Bucca', title: 'Desarrollador', descripcion: 'El siguiente desafio siempre es bienvenido.' },
    { fecha: 'Marcos Broschero', title: 'Desarrollador', descripcion: 'No se trata del auto que conduces, es el conductor quien conduce el auto el que hace la conducción' },
    { fecha: 'Erwin Citadino', title: 'Desarrollador', descripcion: 'El ayer se ha ido. ¿Qué harás hoy?' },
    { fecha: 'Ariadna Coronel', title: 'Desarrolladora', descripcion: 'Si puedes imaginarlo, puedes Programarlo' },
];
</script>

<template>
    <ul>
        <li v-for="(item, index) in educacion" :key="index" :style="{ '--fecha-color': fechaColor[index].color}">
        <div class="fecha">{{ item.fecha }}</div>
        <h3 class="title">{{ item.title }}</h3>
        <div class="descripcion">{{ item.descripcion }}</div>
    </li>
    </ul>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap");
*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  --color: rgb(255, 196, 0);
  --bgColor: rgb(255, 255, 255);
  min-height: 100vh;
  display: grid;
  align-content: center;
  gap: 2rem;
  padding: 2rem;
  font-family: "Poppins", sans-serif;
  color: var(--vt-c-black);
  background: var(----vt-c-black);
}


ul {
    margin-top: 2rem;
  --col-gap: 2rem;
  --row-gap: 2rem;
  --line-w: 0.25rem;
  display: grid;
  grid-template-columns: var(--line-w) 1fr;
  grid-auto-columns: max-content;
  column-gap: var(--col-gap);
  list-style: none;
  width: min(60rem, 90%);
  margin-inline: auto;
}


ul::before {
  content: "";
  grid-column: 1;
  grid-row: 1 / span 20;
  background: rgb(225, 225, 225);
  border-radius: calc(var(--line-w) / 2);
}

ul li:not(:last-child) {
  margin-bottom: var(--row-gap);
}


ul li {
  grid-column: 2;
  --inlineP: 1.5rem;
  margin-inline: var(--inlineP);
  grid-row: span 2;
  display: grid;
  grid-template-rows: min-content min-content min-content;
}


ul li .fecha {
  --dateH: 3rem;
  height: var(--dateH);
  margin-inline: calc(var(--inlineP) * -1);
  text-align: center;
  background-color: var(--fecha-color);
  color: white;
  font-size: 1.25rem;
  font-weight: 700;
  display: grid;
  place-content: center;
  position: relative;
  border-radius: calc(var(--dateH) / 2) 0 0 calc(var(--dateH) / 2);
}

ul li .fecha::before {
  content: "";
  width: var(--inlineP);
  aspect-ratio: 1;
  background: var(--fecha-color);
  background-image: linear-gradient(rgba(0, 0, 0, 0.2) 100%, transparent);
  position: absolute;
  top: 100%;
  clip-path: polygon(0 0, 100% 0, 0 100%);
  right: 0;
}

ul li .fecha::after {
  content: "";
  position: absolute;
  width: 1rem;
  aspect-ratio: 1;
  background: var(--bgColor);
  border: 0.3rem solid var(--fecha-color);
  border-radius: 50%;
  top: 50%;
  transform: translate(50%, -50%);
  right: calc(100% + var(--col-gap) + var(--line-w) / 2);
}

ul li .title,
ul li .descripcion {
  background: var(--bgColor);
  position: relative;
  padding-inline: 1.5rem;
}

ul li .title {
  overflow: hidden;
  padding-block-start: 1.5rem;
  padding-block-end: 1rem;
  font-weight: 500;
}

ul li .descripcion {
  padding-block-end: 1.5rem;
  font-weight: 300;
}


ul li .title::before,
ul li .descripcion::before {
  content: "";
  position: absolute;
  width: 90%;
  height: 0.5rem;
  background: rgb(255, 208, 0);
  left: 50%;
  border-radius: 50%;
  filter: blur(4px);
  transform: translate(-50%, 50%);
}

ul li .title::before {
  bottom: calc(100% + 0.125rem);
}

ul li .descripcion::before {
  z-index: -1;
  bottom: 0.25rem;
}

@media (min-width: 40rem) {
  ul {
    grid-template-columns: 1fr var(--line-w) 1fr;
  }
  ul::before {
    grid-column: 2;
  }
  ul li:nth-child(odd) {
    grid-column: 1;
  }
  ul li:nth-child(even) {
    grid-column: 3;
  }

  ul li:nth-child(2) {
    grid-row: 2/4;
  }

  ul li:nth-child(odd) .fecha::before {
    clip-path: polygon(0 0, 100% 0, 100% 100%);
    left: 0;
  }

  ul li:nth-child(odd) .fecha::after {
    transform: translate(-50%, -50%);
    left: calc(100% + var(--col-gap) + var(--line-w) / 2);
  }

  ul li:nth-child(odd) .fecha {
    border-radius: 0 calc(var(--dateH) / 2) calc(var(--dateH) / 2) 0;
  }
}


.credits {
  margin-top: 1rem;
  text-align: right;
}
.credits a {
  color: var(--color);
}
</style>

<script setup>
import JavaScript from '/src/components/icons/JavaScript.svg';
import Python from "/src/components/icons/Python.svg";
import Java from "/src/components/icons/Java.svg";
import Vuejs from "/src/components/icons/Vue.js.svg";
import Git from "/src/components/icons/Git.svg";
import VSC from "/src/components/icons/VisualStudioCode.svg";
import Postman from "/src/components/icons/postman.svg";
import Jmeter from "/src/components/icons/jmeter.svg";
import MySQL from "/src/components/icons/MySQL.svg";
import Español from "/src/components/icons/arg.svg";
import Ingles from "/src/components/icons/eeuu.svg"

import { ref } from 'vue';
const habilidades = ref([
    {
        id: 1, nombre: 'Lenguajes de Programación', habilidades: [
            { id: 1, nombre: 'JavaScript', nivel: 'En formación', icono: JavaScript },
            { id: 2, nombre: 'Python', nivel: 'En formación', icono: Python },
            { id: 3, nombre: 'Java', nivel: 'En formación', icono: Java },
        ]
    },
    {
        id: 2, nombre: 'Frameworks y Librerías', habilidades: [
            { id: 1, nombre: 'Vue.js', nivel: 'En formación', icono: Vuejs },
         ]
    },
    {
        id: 3, nombre: 'Herramientas y Software', habilidades: [
            { id: 1, nombre: 'Git', nivel: 'En formación', icono: Git },
            { id: 2, nombre: 'Visual Studio Code', nivel: 'En formación', icono: VSC },
            { id: 3, nombre: 'Postman', nivel: 'intermedio', icono: Postman},
            { id: 4, nombre: 'Jmeter', nivel: 'Intermedio', icono: Jmeter },
        ]
    },
    {
        id: 4, nombre: 'Bases de Datos', habilidades: [
            { id: 1, nombre: 'MySQL', nivel: 'Intermedio', icono: MySQL },
        ]
    },
    {
        id: 5, nombre: 'Idiomas', habilidades: [
            { id: 1, nombre: 'Español', nivel: 'Nativo', icono: Español },
            { id: 2, nombre: 'Inglés', nivel: 'B2 + - Upper Intermediate', icono: Ingles }
        ]
    }
]);
</script>

<template>
    <div class="skills-contenedor">
        <div v-for="habilidad in habilidades" :key="habilidad.id" class="skills-categoria">
            <h3>{{ habilidad.nombre }}</h3>
            <ul class="skills">
                <li v-for="habilidad in habilidad.habilidades" :key="habilidad.id" class="skill">
                    <img :src="habilidad.icono" :alt="habilidad.nombre">
                    <span>{{ habilidad.nombre }}: {{ habilidad.nivel }}</span>
                </li>
            </ul>
        </div>
    </div>
</template>

<style scoped>
.skills-contenedor {
    padding: 2rem;
}

.skills-categoria {
    margin-bottom: 20px;
}

.skills-categoria h3 {
    display: flex;
    justify-content: left;
    margin-bottom: 10px;
    font-size: 1.5em;
    color: aliceblue;
    font-size: 1.5em;
    font-weight: bold;
}

.skills {
    display: flex;
    justify-content: space-evenly;
    flex-wrap: wrap;
    gap: 20px;
}

.skill {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    background-color: rgba(109, 28, 28, 0.856);
    padding: 0.3em;
    border-radius: 8px;
    flex: 1 1 200px;
    max-width: 250px;
}

.skill:hover {
    background-color: rgb(255, 196, 0);
}

.skill img {
    width: 35px;
    height: 35px;
}

.skill span {
    font-size: 1em;
    color: #ffffff;
}

.skill:hover {
    font-size: 1.3em;
    transition: 2s ease;
}

@media (max-width: 768px) {
    .skills-categoria h3 {
        justify-content: center;
    }

    .skill {
        justify-content: center;
    }
}
</style>

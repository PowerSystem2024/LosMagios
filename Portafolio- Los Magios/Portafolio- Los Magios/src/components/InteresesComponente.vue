<script setup>
import { ref } from 'vue';
import FondoLineal from './FondoLineal.vue';

const intereses = ref([
    '* Trabajo en Equipo: somos un grupo de amigos donde siempre nos apoyamos y ayudamos a cada integrante por igual, no importa el motivo siempre estamos para ayudar',
    '* Capacitación: en el equipo hay una gran sed de conocimientos y ganas de apreder lo que nos lleva a estar siempre pendientes de lo nuevo',
    '* Programar: nos divierte programar y realizar cada desafio que se nos impone',
    '* Jugar: esto sería totalmente imposible si en nuestro equipo no estaría dispuesto a compartir momentos mas allá del trabajo, jugamos como equipo y trabajamos como equipo',
]);
</script>

<template>
    <div class="intereses-contenedor">
        <FondoLineal />
        <ul class="contenedor-lista">
            <li class="item" v-for="interes in intereses" :key="interes">
                {{ interes }}
            </li>
        </ul>
    </div>
</template>

<style scoped>
    .intereses-contenedor {
    display: flex;
    position: relative;
    margin: 0 auto;
    max-width: 80%;
    padding: 1rem;
}

.contenedor-lista {
    list-style-type: none;
    padding: 1rem;
    margin-bottom: .5rem;
    color: var(--vt-c-white-soft);
    font-size: 1.1rem;
    text-shadow: 3px 3px 6px rgba(255, 255, 255, 0);
}

.item {
    margin-bottom: 1rem;
}
</style>

<template>
      <nav class="navbar">
        <div class="navbar-menu">
          <ul>
            <a v-for="nav in navegacion" :key="nav.nombre" :href="nav.enlace" class="nav-item">{{ nav.nombre }}</a>
          </ul>
        </div>
      </nav>
</template>

<script setup>
import { ref } from 'vue';
const navegacion = ref([
  {id:1, nombre : 'Integrantes', enlace: '#educacion'},
  {id:2, nombre : 'Proyectos', enlace: '#proyectos'},
  {id:3, nombre : 'Habilidades', enlace: '#habilidades'}
]);
</script>

<style scoped>
  .navbar{
    background-color: var(--vt-c-indigo);
    color: #fff;
    padding: 0.5rem 1rem;
    align-items: center;
    }

  .navbar-item {
    color: #ffffff;
    text-decoration: none;
    margin-right: 1rem;
  }

  .navbar-menu{
    display: flex;
    justify-content: flex-end;
  }
  .nav-list{
    list-style: none;
  }
  a{
    border: 1px solid;
    border-color: hsl(46, 100%, 49%);
    /*Elimina lo subrayado de los enlaces y elemementos con clase "Green"*/
    border-radius: 5px;
    text-decoration: none;
    /* Añade una transición suave para los cambios de estilo*/
    transition: 0.4s;
    /* Añade padding alrededor del contenido*/
    padding: 5px;
  }
  a:hover{
  /* Cambia el color de fondo al pasar el moyse sobre un enlace*/
  background-color: hsl(46, 100%, 50%);
  }

  @media (max-width: 760px){
    .navbar-menu{
      display: flex;
      justify-content: flex-end;
      width: 100%;
    }
  }
</style>

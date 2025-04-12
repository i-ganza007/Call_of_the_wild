<template>
    <section class="relative z-200 bg-white lg:pb-20">
        <div class="px-7 py-8 flex flex-col gap-6 lg:items-center">
            <h2 class="text-[#1E2D3B] font-semibold text-5xl lg:text-8xl">SERVICES</h2>
            <div class="bg-[#EDCD1F] h-5 w-25 lg:w-50"></div>
        </div>
        <div class="flex max-sm:flex-col max-sm:gap-5 lg:px-20">
            <services :heading="div1.heading" :image="div1.image" />
            <services :heading="div2.heading" :image="div2.image" />
            <services :heading="div3.heading" :image="div3.image" />
        </div>
    </section>
</template>

<script setup>
import { reactive } from 'vue' 
import services from './servicesComp.vue';

const div1 = reactive({
    heading: 'Preconstruction Planning',
    image: 'lake.jpg'
})

const div2 = reactive({
    heading: "Architectural Modelling",
    image: 'lake.jpg'
})

const div3 = reactive({
    heading: 'Construction Management',
    image: 'lake.jpg'
})
</script>

<template>
    <!-- <div class="fixed top-0 left-0 right-0  z-[900] bg-[#800080] h-1  top-0"></div> -->
    <nav class="relative z-10 flex items-center justify-between h-32 max-sm:bg-[#EDCD1F] max-sm:border-b-20 max-sm:border-[#1E2D3B]">
        <!-- Background split -->
        <div class="lg:absolute lg:inset-0 lg:flex hidden">
            <div class="bg-[#EDCD1F] w-[20%] h-full"></div>
            <div class="bg-[#1E2D3B] w-[80%] h-full"></div>
        </div>

        <!-- Logo section -->
        <div class="flex items-center gap-3 px-4 lg:w-[30%] h-full lg:bg-[#EDCD1F] relative z-20">
            <div class="flex items-center gap-3">
                <svg class="w-10 lg:w-14" preserveAspectRatio="xMidYMid meet" data-bbox="-88.7 -33.025 177.4 181.925" viewBox="-88.7 -33.025 177.4 181.925" height="200" width="200" xmlns="http://www.w3.org/2000/svg" data-type="shape" role="presentation" aria-hidden="true">
                    <g>
                        <path d="M88.4 38V5.1c0-1.3-1.6-2.5-2.8-2.8L.8-32.8c-.6-.3-1.9-.3-2.5 0L-86.8 2.3c-.9.3-1.9 1.6-1.9 2.8V38c0 1.3.6 2.5 1.9 2.8L-46 58l-40.8 17c-1.3.3-1.9 1.6-1.9 2.8v32.9c0 1.3.6 2.5 1.9 2.8L-2 148.6c.4.1 1 .3 1.3.3s.8-.1 1.2-.3l85.4-35.1c1.3-.6 2.8-1.6 2.8-2.8V77.9c0-1.3-1.6-2.5-2.8-2.8L44.4 58l41.4-17.1c1.3-.3 2.6-1.6 2.6-2.9zM-.8 111.1l-40.8-17.4L-.8 76.3 40 93.7-.8 111.1zm0-41.4L-29.3 58-.8 46.3 27.7 58-.8 69.7zm0-31.3L-41.6 21-.8 3.6 40 21-.8 38.4zM-3.3-1.8l-46.2 19.6-28.1-12 74.3-31v23.4zm51.8 19.6L3-1.8v-23.4L77.3 5.5 48.5 17.8zM-82.4 36.1V10.8l74.3 31.6-29.4 12.3-44.9-18.6zm73.1 37l-40.8 17.4-28.5-12 40.8-16.8 28.5 11.4zm-73.1 10.5l79.1 33.2v24.4l-79.1-32.3V83.6zM3 141.1v-24.4l79.1-33.2v25.3L3 141.1zm73.7-62.9l-28.5 12L7.4 73.1l28.5-11.7 40.8 16.8zM36.5 54.5L7.4 42.1 82 10.5v25.3L36.5 54.5z"></path>
                    </g>
                </svg>
                <h2 class="text-2xl lg:text-3xl text-[#1E2D3B]"><strong>SPHERE</strong><br/>CONSTRUCTIONS</h2>
            </div>
        </div>

        <!-- Menu section -->
        <div class="lg:w-[80%] hidden lg:block h-full relative z-20">
            <ul class="flex text-white gap-20 h-full items-center justify-end px-8">
                <li class="text-white hover:text-[#EDCD1F] cursor-pointer">HOME</li>
                <li class="text-white hover:text-[#EDCD1F] cursor-pointer">SERVICES</li>
                <li class="text-white hover:text-[#EDCD1F] cursor-pointer">ABOUT</li>
                <li class="text-white hover:text-[#EDCD1F] cursor-pointer">PROJECTS</li>
                <li class="text-white hover:text-[#EDCD1F] cursor-pointer">CONTACTS</li>
            </ul>
        </div>

        <!-- Mobile menu button -->
        <div class="lg:hidden block px-4">
            <img src="../assets/hamb.png" alt="hamburger menu" width="32px">
        </div>
    </nav>
</template>
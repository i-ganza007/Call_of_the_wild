<template>
    <section class="px-7 pt-10 relative z-200 bg-white">
        <div class="my-7">
            <div class="flex flex-col gap-4">
                <h1 class="text-[#1E2D3B] text-5xl font-semibold">Inquiries</h1>
                <p class="text-xl font-medium lg:w-[50%]">
                    For any inquiries, questions or commendations, please call: 123-456-7890 or fill out the following form
                </p>
            </div>
        </div>

        <h1 class="text-[#1E2D3B] text-5xl font-semibold pb-5">Contact Us</h1>

        <div class="flex flex-col gap-4 lg:grid lg:grid-cols-2 lg:grid-rows-2 lg:grid-flow-col lg:justify-items-stretch lg:gap-40">
            <form action="" class="">
                <div class="flex flex-col gap-2">
                    <label for="first-name" class="text-2xl text-[#1E2D3B]">First Name *</label>
                    <input type="text" name="first-name" id="first-name" class="bg-blue-100 h-17 border-1 ">
                </div>

                <div class="flex flex-col gap-2">
                    <label for="last-name" class="text-2xl text-[#1E2D3B]">Last Name *</label>
                    <input type="text" name="last-name" id="last-name" class="bg-blue-100 h-17 border-1">
                </div>

                <div class="flex flex-col gap-2">
                    <label for="email" class="text-2xl text-[#1E2D3B]">Email *</label>
                    <input type="email" name="email" id="email" class="bg-blue-100 h-17 border-1">
                </div>

                <div class="flex flex-col gap-2">
                    <label for="subject" class="text-2xl text-[#1E2D3B]">Subject</label>
                    <input type="text" name="subject" id="subject" class="bg-blue-100 h-17 border-1">
                </div>

                <div class="flex flex-col gap-2">
                    <label for="message" class="text-2xl text-[#1E2D3B]">Message</label>
                    <input type="text" name="subject" id="subject" class="bg-blue-100 h-20 border-1">
                </div>

                <div>
                    <button class="font-semibold text-[#EDCD1F] text-xl bg-gray-800 w-full mt-5 py-5 transition ease-in-out delay-80 hover:bg-[#EDCD1F] hover:text-[#1E2D3B]">Submit</button>
                </div>
            </form>

            <div class="text-[#1E2D3B] flex flex-col gap-9 order-1">
                <div>
                    <h1 class="text-[#1E2D3B] text-5xl font-semibold pb-5">Head Office</h1>
                    <p class="text-3xl">500 Terry Francine Street</p>
                    <p class="text-3xl">San Francisco, CA 94158</p>
                </div>

                <div class="text-3xl">
                    <p>info@mysite.com</p>
                    <p>Tel: 123-456-7890</p>
                    <p>Fax: 123-456-7890</p>
                </div>
            </div>

            <div class="lg:justify-self-end-safe">
                <h1 class="text-[#1E2D3B] text-5xl font-semibold pb-5">Employment</h1>
                <p class="text-3xl text-[#1E2D3B]">To apply for a job with Sphere Constuctions, please send a cover letter together with your C.V. to: info@mysite.com
                </p>

                <div class="mt-8">
                    <div class="bg-[#EDCD1F] h-5 w-25 mb-3"></div>
                    <h1 class="text-[#1E2D3B] text-2xl font-bold pb-5">Get a quote: 123-456-7890</h1>
                </div>
            </div>
        </div>
    </section>
</template>
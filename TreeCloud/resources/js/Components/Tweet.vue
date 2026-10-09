<script setup>
import { onMounted, ref } from 'vue';
import { Link } from '@inertiajs/vue3';
import HeartOutline from 'vue-material-design-icons/HeartOutline.vue'
import ChartBar from 'vue-material-design-icons/ChartBar.vue'
import MessageOutline from 'vue-material-design-icons/MessageOutline.vue'
import Sync from 'vue-material-design-icons/Sync.vue'
import DotsHorizontal from 'vue-material-design-icons/DotsHorizontal.vue'
import TrashCanOutline from 'vue-material-design-icons/TrashCanOutline.vue'

defineProps({ tweet: Object });

let openOptions = ref(false);

</script>

<template>
    <div class="min-w-[60px]">
        <img class="rounded-full m-2 mt-3" width="50" :src="tweet.image">
    </div>
    <div class="p-2 w-full">
        <div class="font-extrabold flex items-center justify-between mt-0.5 mb-1.5">
            <div class="flex items-center">
                <div>{{ tweet.name }}</div>
                <span class="font-[300] text-[15px] text-gray-500 pl-2">{{ tweet.handle }}</span>
            </div>
            <div class="hover:bg-white/10 rounded-full cursor-pointer relative transition-colors">
                <button type="button" class="block p-2">
                    <DotsHorizontal @click="openOptions = !openOptions" />
                </button>
                <div v-if="openOptions" class="absolute mt-1 right-0 w-[200px] glass border border-brand-border rounded-xl shadow-2xl z-50 overflow-hidden">
                    <ul class="p-2">
                        <Link
                            as="button"
                            method="delete"
                            :href="route('tweets.destroy', { id: tweet.id })"
                            class="flex items-center cursor-pointer w-full hover:bg-red-500/10 p-2 rounded-lg transition-colors"
                        >
                            <TrashCanOutline class="pr-3" fillColor="#EF4444" :size="18"/>
                            <span class="text-red-500 font-bold">Delete</span>
                        </Link>
                    </ul>
                </div>
            </div>
        </div>
        <div class="pb-3">{{ tweet.tweet }}</div>
        <div v-if="tweet.file">
            <div v-if="!tweet.is_video" class="rounded-xl">
                <img :src="tweet.file" class="mt-2 object-fill rounded-xl w-full">
            </div>
            <div v-else>
                <video class="rounded-xl" :src="tweet.file" controls></video>
            </div>
        </div>
        <div class="flex items-center justify-between mt-4 w-4/5 text-gray-400">
            <div class="flex items-center group cursor-pointer">
                <div class="p-2 rounded-full group-hover:bg-brand-accent/10 group-hover:text-brand-accent transition-colors">
                    <MessageOutline class="transition-colors" :size="18" />
                </div>
                <span class="text-xs font-semibold ml-1 group-hover:text-brand-accent transition-colors">{{ tweet.comments }}</span>
            </div>
            <div class="flex items-center group cursor-pointer">
                <div class="p-2 rounded-full group-hover:bg-green-500/10 group-hover:text-green-500 transition-colors">
                    <Sync class="transition-colors" :size="18" />
                </div>
                <span class="text-xs font-semibold ml-1 group-hover:text-green-500 transition-colors">{{ tweet.retweets }}</span>
            </div>
            <div class="flex items-center group cursor-pointer">
                <div class="p-2 rounded-full group-hover:bg-pink-500/10 group-hover:text-pink-500 transition-colors">
                    <HeartOutline class="transition-colors" :size="18" />
                </div>
                <span class="text-xs font-semibold ml-1 group-hover:text-pink-500 transition-colors">{{ tweet.likes }}</span>
            </div>
            <div class="flex items-center group cursor-pointer">
                <div class="p-2 rounded-full group-hover:bg-brand-accent/10 group-hover:text-brand-accent transition-colors">
                    <ChartBar class="transition-colors" :size="18" />
                </div>
                <span class="text-xs font-semibold ml-1 group-hover:text-brand-accent transition-colors">{{ tweet.analytics }}</span>
            </div>

        </div>
    </div>
</template>

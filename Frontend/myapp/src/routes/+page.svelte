<script>
    import { onMount } from "svelte";
    import Home from "$lib/home.svelte";
    export let data;
    console.log(data.path)
</script>

<Home directories={data.directories} files={data.files} path={data.path}/>

<style>
    :global(:root) {
        padding: 2rem 6rem 6rem 6rem;
    }
</style>

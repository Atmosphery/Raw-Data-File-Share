<script>
    import { onMount } from "svelte";
    import Home from "$lib/home.svelte";
    export let data;
    //console.log(data)
</script>

<Home data={data}/>

<style>
    :global(:root) {
        padding: 2rem 6rem 6rem 6rem;
    }
</style>

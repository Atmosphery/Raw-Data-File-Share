<script>
    import { json } from "@sveltejs/kit";
    import { Router, Link, Route } from "svelte-routing";
    import {load_tree} from "$lib/tools.js"
    import FileExplorer from './file_explorer.svelte'
    import { onMount } from "svelte";
    export let data;
    console.log(data);
    let directories = data.directories;
    let files = data.files;
    let path = data.path;

    const update = (path) =>{
        console.log(path)
        data = load_tree(path)
        console.log(data);
    }
</script>

<!-- {#key data} -->
    
        <nav>
            {#each directories as directory}
                <div>
                    <Link to={`/${path}/${directory}`} >{directory}</Link>
                </div>
                <Route path={`/${path}/${directory}`} component={FileExplorer} />
            {/each}
        </nav>
    
<!-- {/key} -->

<style>
    button {
        all: unset
    }
</style>

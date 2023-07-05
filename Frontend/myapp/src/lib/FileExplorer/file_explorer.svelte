<script>
    import { json } from "@sveltejs/kit";
    import { Router, Link, Route } from "svelte-routing";
    export let data;
    console.log(data);
    let directories = data.directories;
    let files = data.files;
    let path = data.path;
</script>

<Router>
    <nav>
        {#each directories as directory}
        <div>
            <Link to={`/${path}/${directory}`}>{directory}</Link>
        </div>
        {/each}
    </nav>
</Router>
<p />

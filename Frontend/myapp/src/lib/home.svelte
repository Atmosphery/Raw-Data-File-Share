<script>
    import { onMount } from "svelte";
    import file from "svelte-awesome/icons/file";
    import { host } from "$lib/tools.js";
    import FileExplorer from "./FileExplorer/file_explorer.svelte";
    import { writable } from "svelte/store"
    export let data;
    
</script>

<h1>Welcome to SvelteKit</h1>
<p>
    Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation
</p>

<form>
    <input
        type="file"
        name="file_upload"
        class="file_upload"
        multiple={true}
    /><br />
    <input type="button" value="Submit Files" />
    <FileExplorer data={data}/>
</form>


<script>
	import Icon from "svelte-awesome";
	import folder from "svelte-awesome/icons/folder";
	import { Route, Router, Link } from "svelte-routing";
	export let directory_name;
	export let path;
	
	
</script>

<div class="directory">
	<div class="directory_icon">
		<Icon data={folder} label="folder" scale={2} />
	</div>
	<div class="directory_name" name="directory_name">
		<Link href={path == "/" ? directory_name : `${path}/${directory_name}`}
			>{directory_name}</Link
		>
	</div>
</div>

<style>
	.directory {
		display: flex;
		border: solid 2px black;
		align-items: center;
		padding-left: 1rem;
		padding-right: 1rem;
	}

	.directory_name {
		padding-left: 1rem;
	}
</style>

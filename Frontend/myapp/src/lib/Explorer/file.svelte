<script>
	export let file_name;
	export let date_modified;
	import { Icon } from "svelte-awesome";
	import file from "svelte-awesome/icons/file";
</script>

<div class="file">
	<div class="directory_icon">
		<Icon data={file} label="file" scale={2} />
	</div>
	<a href={host + `tree/${file_name}`} class="file_name" name="file_name">{file_name}</a>
	<p name="date_modified">{date_modified}</p>
</div>

<style>
	.file {
		display: flex;
		border: solid 2px black;
		align-items: center;
		padding-left: 1rem;
		padding-right: 1rem;
	}

	.file_name {
		flex: 2;
		padding-left: 1rem;
	}

	p {
		padding-right: 1rem;
	}
</style>

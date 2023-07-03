import { error } from '@sveltejs/kit';
import path from 'path';


export async function load({params, url}) {
	const response = await fetch(`http://127.0.0.1:5000/tree`);
	let json = await response.json();
	let directories = json[1];
	let files = json[2];
	if (!json) throw error(404);
	console.log(url)
	return {
		directories,
		files,
		path: url.pathname
	};
}

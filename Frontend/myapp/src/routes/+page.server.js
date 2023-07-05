import { error } from '@sveltejs/kit';
import path from 'path';


export async function load({ params, url }) {
	const response = await fetch(`http://127.0.0.1:5000/tree`);
	let json = await response.json();
	return {
		path: json[0],
		directories: json[1],
		files: json[2]
	}
}

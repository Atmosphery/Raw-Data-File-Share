export const host = "http://127.0.0.1:5000/"

export async function load_tree(path) {
	const response = await fetch(`http://127.0.0.1:5000/tree/${path}`);
	let json = await response.json();
	let directories = json[1];
	let files = json[2];
	if (!json) throw error(404);
	return {
		directories,
		files
	};
}
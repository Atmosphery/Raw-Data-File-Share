export const host = "http://127.0.0.1:5000/"

export async function load_tree(path) {
	const response = await fetch(`http://127.0.0.1:5000/tree/${path}`);
	let json = await response.json();
	return {
		path: json[0],
		directories: json[1],
		files: json[2]
	}
}


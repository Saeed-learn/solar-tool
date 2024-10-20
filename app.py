import streamlit as st
import streamlit.components.v1 as components

# Title of the Streamlit app
st.title("Interactive 3D Roof Model with Three.js")

# Location input
st.subheader("Select Location")
lat = st.number_input("Enter Latitude", -90.0, 90.0, 0.0, format="%.6f")
lon = st.number_input("Enter Longitude", -180.0, 180.0, 0.0, format="%.6f")

# Show the location on a map
st.map(data={"lat": [lat], "lon": [lon]}, zoom=10)

# Sliders to control the size of the cube (representing the roof)
width = st.slider("Select Roof Width", 1, 10, 2)
height = st.slider("Select Roof Height", 1, 10, 2)
depth = st.slider("Select Roof Depth", 1, 10, 2)

# Pass the values to the JavaScript part by writing a new HTML template
html_code = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3D Roof Model</title>
    <style>
        body {{ margin: 0; }}
        canvas {{ display: block; }}
    </style>
</head>
<body>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

    <script>
        // Create a scene
        const scene = new THREE.Scene();

        // Create a camera
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
        camera.position.z = 10;

        // Create a renderer
        const renderer = new THREE.WebGLRenderer();
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        // Add a cube to represent the roof with dynamic dimensions
        const geometry = new THREE.BoxGeometry({width}, {height}, {depth});
        const material = new THREE.MeshBasicMaterial({{ color: 0x00ff00 }});  // Use double curly braces to escape
        const cube = new THREE.Mesh(geometry, material);
        scene.add(cube);

        // Render the scene
        function animate() {{
            requestAnimationFrame(animate);
            cube.rotation.x += 0.01;
            cube.rotation.y += 0.01;
            renderer.render(scene, camera);
        }}
        animate();
    </script>
</body>
</html>
"""

# Use Streamlit components to display the HTML content dynamically
components.html(html_code, height=600)

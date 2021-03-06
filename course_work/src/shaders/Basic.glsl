#shader vertex
#version 330 core
layout (location = 0) in vec3 aPos;
layout (location = 1) in vec3 aNorm;

out vec3 FragPos;
out vec3 Normal;

uniform mat4 view;
uniform mat4 projection;

void main(){
    FragPos = aPos;
    Normal = aNorm;
    gl_Position = projection * view * vec4(aPos.x, aPos.y, aPos.z, 1.0);
}

#shader fragment
#version 330 core
out vec4 FragColor;

in vec3 FragPos;
in vec3 Normal;

/* uniform vec3 viewPos; */

vec3 lightColor = vec3(1.0, 1.0, 1.0);
vec3 objectColor = vec3(1.0, 0.5, 0.2);
vec3 lightPos = vec3(1.0, 1.0, 1.0);


void main(){
    float ambientStrength = 0.3;
    vec3 ambient = ambientStrength * lightColor;

    vec3 norm = normalize(Normal);
    vec3 lightDir = normalize(lightPos - FragPos);
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;

    /* float specularStrength = 0.5;
    vec3 viewDir = normalize(viewPos - FragPos);
    vec3 reflectDir = reflect(-lightDir, norm);
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32);
    vec3 specular = specularStrength * spec * lightColor; */

    vec3 result = (ambient + diffuse /* + specular*/) * objectColor;

    FragColor = vec4(result, 1.0);
}

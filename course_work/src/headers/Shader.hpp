#ifndef SHADER_HPP
#define SHADER_HPP

#include <string>
#include <glm/glm.hpp>

struct ShaderProgramSource {
    std::string VertexSource;
    std::string FragmentSourse;
};

class Shader {
private:
    std::string m_FilePath;
    unsigned int m_RendererID;


public:
    Shader(const std::string& filepath);
    ~Shader ();

    void Bind();
    void Unbind();
    void SetUniform4f(const std::string& name, float v0, float v1, float v2, float v3);
    void SetMat4(const std::string &name, const glm::mat4 &mat);
    void SetVec3(const std::string &name, const glm::vec3 &value);


private:
    unsigned int CompileShader(unsigned int type, const std::string& sourse);
    unsigned int CreateShader(const std::string& vertexShader, const std::string& fragmentShader);
    ShaderProgramSource ParseShader(const std::string& filepath);
    unsigned int GetUniformLocation(const std::string& name);
};

#endif

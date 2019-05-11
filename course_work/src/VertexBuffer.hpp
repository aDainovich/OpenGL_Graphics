#ifndef VERTEXBUFFER_HPP
#define VERTEXBUFFER_HPP

class VertexBuffer {
private:
    unsigned int m_RendererID;

public:
    VertexBuffer (const void* data, unsigned int size){
        glGenBuffers(1, &m_RendererID);
        glBindBuffer(GL_ARRAY_BUFFER, m_RendererID);
        glBufferData(GL_ARRAY_BUFFER, size, data, GL_STATIC_DRAW);
    }
    ~VertexBuffer (){
         glDeleteBuffers(1, &m_RendererID);
    }

    void Bind() const {
        glBindBuffer(GL_ARRAY_BUFFER, m_RendererID);
    }
    void Unbind() const {
        glBindBuffer(GL_ARRAY_BUFFER, 0);
    }
};

#endif

from arcade.experimental.texture_render_target import RenderTargetTexture


class TrackPathShader(RenderTargetTexture):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.program = self.ctx.program(
            vertex_shader="""
            #version 330

            in vec2 in_vert;
            in vec2 in_uv;
            out vec2 uv;

            void main() {
                gl_Position = vec4(in_vert, 0.0, 1.0);
                uv = in_uv;
            }
            """,

            fragment_shader="""
            #version 330

            uniform sampler2D texture0;

            in vec2 uv;
            
            out vec4 fragColor;

            float line(vec2 a, vec2 b, vec2 p, float w)
            {
                vec2 pa = p - a;
                vec2 ba = b - a;
                float t = clamp( dot(pa,ba)/dot(ba,ba), 0.0, 1.0 );
                vec2 c = a + ba*t;
                float d = length(c - p);                
                return smoothstep( d, 0.0, d-w*0.005 );
            }

            void main() {
                float w = 0.005;
                vec4 color = texture(texture0, uv);
                vec4 color2 = vec4(0.0);
                vec4 black = vec4(0.0,0.0,0.0,1.0);
                vec4 glow = vec4(1.0,1.0,0.0,1.0);
                if(color == black){
                    float count=0;
                    for(float d=w/5;d<=w;d+=w/5){
                        // up
                        color2 = texture(texture0, uv+vec2(0.0,d));
                        if(color2 != black){
                            count += 1.0/d;
                        }
                        // down
                        color2 = texture(texture0, uv+vec2(0.0,-d));
                        if(color2 != black){
                            count += 1.0/d;
                        }                        
                        // left
                        color2 = texture(texture0, uv+vec2(-d,0.0));
                        if(color2 != black){
                            count += 1.0/d;
                        }
                        // right
                        color2 = texture(texture0, uv+vec2(d,0.0));
                        if(color2 != black){
                            count += 1.0/d;
                        }       
                    }
                    color = glow;
                    color.a = count / 2000.0;
                }                
                fragColor = color;
            }
            """,
        )
#        self.program["view_ratio"] = 1.0

    def setViewRatio(self, value):
        self.program["view_ratio"] = value

    def setTrackPath(self, posA, posB, posC, posD, posE):
        self.program["posA"] = posA
        self.program["posB"] = posB
        self.program["posC"] = posC
        self.program["posD"] = posD
        self.program["posE"] = posE

    def use(self):
        self._fbo.use()

    def draw(self):
        self.texture.use(0)
        self._quad_fs.render(self.program)

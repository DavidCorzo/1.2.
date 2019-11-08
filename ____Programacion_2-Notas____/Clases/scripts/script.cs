public class PadController : Monobehaviour
{
    Vector3 pos;
    // start in called once per frame
    void Start() {
        pos = new vector3(0.0f,0.0f,0.0f);
    }
    // updates every frame
    void update() {
        Pos = this.transtform.position;
        If (Input.GetKeyDown("w")){
            pos.y++;
        }
        this.transtform.position = pos;
    }
}

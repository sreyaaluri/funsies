#include <iostream>
#include <vector>

using namespace std;

class Vert {
  public:
    int index;
    int deg;
    int m;
    Vert* parent = nullptr;
    inline void print(){ cout << "i:" << index << "deg: " << deg << "m: " << m << "parent: " << parent->index << endl; }
    Vert() {};
    Vert(int index, int deg, int m) : index(index), deg(deg), m(m) {};
};

int main() {
  int n = -1;
  while(n != 0){
    cout << "n: " << endl;
    cin >> n;
    vector<Vert> vect(n);
    for(int i = 0; i < n; i++){
      int m;
      int d;
      cin >> m;
      cin >> d;
      vect[i] = Vert(i, d, m);
      for(int j = 0; j < d; j++){
        int v;
        cin >> v;
        // vect[v-1].parent = *vect[i];
      }
    }
    for(int i = 0; i < vect.size(); i++){ vect[i].print(); }
  }

}
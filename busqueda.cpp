#include <iostream>
#include <vector>
#include <chrono>
using namespace std;

int busquedaLineal(const vector<long long>& a, long long x, long long& ops) {
    ops = 0;
    for (size_t i=0; i<a.size(); ++i) {
        ++ops;
        if (a[i] == x) return static_cast<int>(i);
    }
    return -1;
}

int busquedaBinaria(const vector<long long>& a, long long x, long long& ops) {
    int izq=0, der=static_cast<int>(a.size())-1;
    ops=0;
    while (izq <= der) {
        int medio = izq + (der-izq)/2;
        ++ops;
        if (a[medio] == x) return medio;
        if (a[medio] < x) izq = medio+1;
        else der = medio-1;
    }
    return -1;
}

int main() {
    vector<long long> datos;
    for (long long i = 0; i < 20; ++i) datos.push_back(i);
    long long objetivo = 15;
    long long ops;

    auto inicio = chrono::high_resolution_clock::now();
    int pos = busquedaLineal(datos, objetivo, ops);
    auto fin = chrono::high_resolution_clock::now();
    auto tiempo_ns = chrono::duration_cast<chrono::nanoseconds>(fin - inicio).count();
    cout << "Lineal  -> posicion=" << pos << ", comparaciones=" << ops << ", tiempo_ns=" << tiempo_ns << endl;

    inicio = chrono::high_resolution_clock::now();
    pos = busquedaBinaria(datos, objetivo, ops);
    fin = chrono::high_resolution_clock::now();
    tiempo_ns = chrono::duration_cast<chrono::nanoseconds>(fin - inicio).count();
    cout << "Binaria -> posicion=" << pos << ", comparaciones=" << ops << ", tiempo_ns=" << tiempo_ns << endl;

    return 0;
}

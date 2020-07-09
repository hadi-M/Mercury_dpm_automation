#include <iostream>
#include <typeinfo>

// int main(int argc, char** argv) {
int main() {
    std::ifstream t("file.txt");
    std::stringstream buffer;
    buffer << t.rdbuf();
}
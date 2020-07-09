#include <string>
#include <fstream>
#include <streambuf>
#include <iostream>
#include <sstream>

int main()
{
    std::ifstream t1("single_U_0.txt");
    std::ifstream t2("single_u_0.txt");
    std::ifstream t3("single_epsilon_0.txt");

    std::stringstream buffer;

    buffer << t1.rdbuf();
    double U_0 = std::stod(buffer.str());
    std::cout << U_0 << std::endl;

    
    // buffer << t1.rdbuf();    


    // std::string s = "scott\ntiger\nmushroom";
    // std::string delimiter = "\n";

    // size_t pos = 0;
    // std::string token;
    // while ((pos = s.find(delimiter)) != std::string::npos)
    // {
    //     token = s.substr(0, pos);
    //     std::cout << token << std::endl;
    //     s.erase(0, pos + delimiter.length());
    // }
    // std::cout << s << std::endl;
}

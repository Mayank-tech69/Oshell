#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <filesystem>
#include <fstream>
#include <cstdlib>
#include <cstdio>
#include <unistd.h>

using namespace std;
namespace fs = std::filesystem;

std::filesystem::path prev_dir = fs::current_path();





void execute_command(const vector<string>& args);

// splitting the string into words for execution of commands

vector<string> parse_input(const string& input) {
    vector<string> tokens;
    istringstream stream(input);
    string token;
    while (stream >> token) {
        tokens.push_back(token);
    }
    return tokens;
}
// main function


int main() {
    while (true) {
        cout << "Current Working Directory: " << fs::current_path() << endl;
        cout << "# ";
        string input;
        getline(cin, input);

        if (input.empty()) continue;

        vector<string> args = parse_input(input);

        if (args[0] == "exit") {
            exit(0);
        }

        execute_command(args);
    }

    return 0;
}

// function to execute every command in our shell

void execute_command(const vector<string>& args) {
    if (args.empty()) return;

    const string& command = args[0];

    if (command == "speak") {
        for (size_t i = 1; i < args.size(); ++i) {
            cout << args[i] << " ";
        }
        cout << endl;
        return;
    }

    if (command == "type") {
        for (size_t i = 1; i < args.size(); ++i) {
            cout << args[i] << " is a command" << endl;
        }
        return;
    }

    if (command == "clear") {
        #ifdef _WIN32
            system("cls");
        #else
            system("clear");
        #endif

        return;
    }

    if (command == "ls") {
        for (const auto& entry : fs::directory_iterator(fs::current_path())) {
            cout << entry.path().filename() << endl;
        }
        return;
    }

    if (command == "makedir") {
        if (args.size() < 2) {
            cout << "Error: No directory specified!" << endl;
            return;
        }
        try {
            fs::create_directory(args[1]);
            cout << "Directory created: " << args[1] << endl;
        } catch (const fs::filesystem_error& e) {
            cout << "Error: " << e.what() << endl;
        }
        return;
    }

    if (command == "removedir") {
        if (args.size() < 2) {
            cout << "Error: No directory specified!" << endl;
            return;
        }
        try {
            fs::remove_all(args[1]);
            cout << "Directory removed: " << args[1] << endl;
        } catch (const fs::filesystem_error& e) {
            cout << "Error: " << e.what() << endl;
        }
        return;
    }

    if (command == "changedir") {
        if (args.size() < 2) {
            cout << "Error: No directory specified!" << endl;
            return;
        }
        try {
            prev_dir = fs::current_path();
            fs::current_path(args[1]);
            cout << "Directory changed to: " << fs::current_path() << endl;
        } catch (const fs::filesystem_error& e) {
            cout << "Error: " << e.what() << endl;
        }
        return;
    }

    if (command == "curdir") {
        cout << fs::current_path() << endl;
        return;
    }

    if (command == "createfile") {
        if (args.size() < 2) {
            cout << "Error: No file specified!" << endl;
            return;
        }
        ofstream file(args[1]);
        if (file) {
            cout << "File created: " << args[1] << endl;
        } else {
            cout << "Error creating file: " << args[1] << endl;
        }
        return;
    }

    if (command == "delfile") {
        if (args.size() < 2) {
            cout << "Error: No file specified!" << endl;
            return;
        }
        if (fs::remove(args[1])) {
            cout << "File deleted: " << args[1] << endl;
        } else {
            cout << "Error deleting file: " << args[1] << endl;
        }
        return;
    }

    if (command == "writefile") {
        if (args.size() < 2) {
            cout << "Error: No file specified!" << endl;
            return;
        }
        cout << "Enter content: ";
        string content;
        getline(cin, content);
        ofstream file(args[1]);
        if (file) {
            file << content;
            cout << "Data written to file: " << args[1] << endl;
        } else {
            cout << "Error writing to file: " << args[1] << endl;
        }
        return;
    }

    if (command == "appendfile") {
        if (args.size() < 2) {
            cout << "Error: No file specified!" << endl;
            return;
        }
        cout << "Enter content: ";
        string content;
        getline(cin, content);
        ofstream file(args[1], ios::app);
        if (file) {
            file << content;
            cout << "Data appended to file: " << args[1] << endl;
        } else {
            cout << "Error appending to file: " << args[1] << endl;
        }
        return;
    }

    if (command == "copyfile") {
        if (args.size() < 2) {
            cout << "Error: Specify source and destination files!" << endl;
            return;
        }
        try {
            // fs::copy_file(args[1], args[2], fs::copy_options::update_existing);
            string line;
            ifstream init_file(args[1]);
            ofstream final_file(args[2]);
            if (init_file && final_file){
                while(getline(init_file,line)){
                    final_file << line << '\n';
                }
            }
            cout << "File copied from " << args[1] << " to " << args[2] << endl;
        } catch (const fs::filesystem_error& e) {
            cout << "Error: " << e.what() << endl;
        }
        return;
    }

    if (command == "help") {
        cout << "Available Commands:\n";
        cout << "  speak <message>         - Prints the message to the console\n";
        cout << "  type <command>          - Checks if a command exists\n";
        cout << "  clear                   - Clears the console\n";
        cout << "  ls                      - Lists files in the current directory\n";
        cout << "  makedir <dir>           - Creates a directory\n";
        cout << "  removedir <dir>         - Deletes a directory and its contents\n";
        cout << "  changedir <dir>         - Changes the current directory\n";
        cout << "  curdir                  - Prints the current working directory\n";
        cout << "  createfile <file>       - Creates an empty file\n";
        cout << "  delfile <file>          - Deletes a file\n";
        cout << "  writefile <file>        - Writes user input to a file\n";
        cout << "  appendfile <file>       - Appends user input to a file\n";
        cout << "  copyfile <src> <dest>   - Copies a file\n";
        cout << "  readfile <file>         - Displays file content\n";
        cout << "  renamefile <old> <new>  - Renames a file\n";
        cout << "  exit                    - Exits the shell\n";
        cout << "  help                  - Displays this help message\n";
        return;
    }
    

    if (command == "readfile"){
        if(args.size()<2){
            cout<<"Error: Specify file name to be read"<< endl;
            return;
        }

        ifstream file(args[1]);
        if (file){
            string line;
            cout<<"Contents of file are:"<<endl;
            while(getline(file,line)){
                cout<<line<<endl;
            }

        }
        else{
            cout<<"Error Opening file"<<endl;
        
        }
        return;

        
    }

    if (command == "renamefile"){
        if(args.size() < 3){
            cout<<"Error: Mention the old file name and new file name"<<endl;
            return;
        }
        
        string oldfilename = args[1];
        string newfilename = args[2];
        rename(oldfilename.c_str(),newfilename.c_str());
        cout<<"File renamed Successfully"<<endl;
        return;
    }

   cout << "Command Not Found"<<endl;
}

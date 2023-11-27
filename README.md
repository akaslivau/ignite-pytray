# ignite-pytray
This is a simple python script to help you manage Apache Ignite cluster on Windows system.
Sometimes you don't want to use Docker, so it's rather dreary to run different bin/ scripts using command line.

To use this script you need:
1. Installed python3
2. IGNITE_HOME variable to your Apache Ignite (Example: C:\Users\Andrew\Desktop\NewIgnite\apache-ignite-2.15.0-bin)

   You can use Powershell to set it in one line:
   ```[System.Environment]::SetEnvironmentVariable('IGNITE_HOME','C:\Users\Andrew\Desktop\NewIgnite\apache-ignite-2.15.0-bin', 'Machine')```

For auto startup:
1. Win + R
2. shell:startup
3. Put link on your script inside this folder

Base script functionality. You can extend it if neccessary.
1. Baseline
2. Start cluster (default 2 nodes) + activate
3. Start node + activate it
4. Stop all -- kill all open ignite windows
5. Hard reset -- clear all work logs, metadata, binary etc
6. Exit. Just exit

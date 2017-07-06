# codebreaker-assistant

A command line tool to help in solving the newspaper puzzle "Codebreaker"\*, written in Python3.

\* Also known as "Codeword" and "Code Cracker" puzzles.

## Getting Started

This project consists of the following two files.
* `CodebreakerAssistant.py` - The command line interface Python script.
* `wordsEnDictPickle.txt` - A preprocessed dictionary mapping word templates to the English words of that form.

These files must be present in the same directory to run.

### Prerequisites

To run target-solver, the host machine must have the following installed:
* `Python3` - The programming language in which codebreaker-assistant was written. Available [here](https://www.python.org/).

### Running

The tool may be started by running the script `TargetSolver.py` as follows:  
`python3 CodebreakerAssistant.py` 

The response will be a prompt for a word template, described in Section "Use".

### Use

The Codebreaker puzzle provides the player with a crossword-like board with a few letters entered, and no clues. Every cell is given a number in [1, 26]. The objective is to fill the board where every cell with the same number holds the same letter.

codebreaker-assistant helps to solve these puzzles by listing all words that follow a given template.

A word template is any collection of letters and symbols where:
* Letters (upper or lower case) are locked in in that position.
* Symbols may represent any letter not already locked in.
* All instances of the same symbol represent the same letter.

For example, the following row provides three locked-in letters, and two unknown (which must be represented by other symbols).

<table align="center">
    <tr>
        <td align="center"><sup>1</sup>P</td>
        <td align="center"><sup>2</sup>U</td>
        <td align="center"><sup>3</sup> </td>
        <td align="center"><sup>3</sup> </td>
        <td align="center"><sup>4</sup>L</td>
        <td align="center"><sup>5</sup> </td>
    </tr>
</table>

The above clue may be represented by any of the following templates:  
`pu33l5`  
`PU11L2`  
`Pu**L#`  
Entering any of the above templates in the codebreaker-assistant prompt results in the following output:  
`['puddle', 'puddly', 'puzzle']`  
A literal Python list of the valid English words with that form. As there is more than one suggestion, other puzzle words should be solved first, to lock in more letters.

## Authors

* **Marc Katzef** - [mkatzef](https://github.com/mkatzef)

#!/usr/bin/env python3

import github

def makeProject(name, description, license):
    """Creates a new github project with the information provided

    Args:
        name: The name to use when creating the github Project
        description: A description of what the idea. The contents will be
            written to the NOTES files.
        license: The license to include in the new github project.

    Returns:
        If the new project was successfully created.
    """
    # TODO: Implement

def banner():
    """Creates the banner for the CLI prompt.

    Returns:
        A string containing the anscii art to draw
    """
    handle = open('resources/banner.txt', mode='rt', encoding='utf-8')
    return handle.read()

def prompt(banner, options):
    """Displays a CLI prompt that asks the user for information on the side
    project idea.

    Args:
        banner: A string containing the anscii art banner to show at run time.
        options: A dict of license options to choose from indexed by number.

    Returns:
        Nothing
    """
    print(banner)
    print("Let's make sure you don't forget that idea!\n")
    correct = False
    while not correct:
        print('Please enter project name:')
        name = input('>> ')
        print('Project description:')
        description = input('>> ')
        print('Choose a license (Enter the number):')
        print('  1. MIT')
        print('  2. Apache 2.0')
        print('  3. GPL')
        license = input('>> ') #TODO: Validate
        print('Lets review your input.\n')
        print('  Name: ', name)
        print('  Description: ', description)
        print('  License: ', options[int(license)])
        print('Is everything correct? (yes, no)')
        ok = input('>> ')
        if ok.lower() == 'yes':
            correct = True
            makeProject(name, description, license)
            print('Great, visit your github profile https://www.github.com/')
        else:
            print('Woops, lets go over the information again!')


def main():
    options = {
        1: 'MIT',
        2: 'Apache 2.0',
        3: 'GPL'
    }
    prompt(banner(), options)


if __name__ == '__main__':
    main()

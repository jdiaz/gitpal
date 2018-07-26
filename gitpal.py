#!/usr/bin/env python3

import github

LICENSES =  {
    1: 'Apache 2.0',
    2: 'BSD 3-Clause "New" pr "Revised" license',
    3: 'GNU General Public License (GPL)',
    4: 'GNU Library or "Lesser" General Public License (LGPL)',
    5: 'MIT license',
    6: 'Mozilla Public License 2.0',
    7: 'Common Development and Distribution License',
    8: 'Eclipse Public License'
}

def make_project(name, description, license):
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
    print('Booting...\n')
    git = github.Github()
    print("Let's make sure you don't forget that idea!\n")
    correct = False
    cli_prompt = '>> '
    while not correct:
        print('Please enter project name:')
        name = input(cli_prompt)
        print('Project description:')
        description = input(cli_prompt)
        print('Choose a license (Enter the number):')
        print(options_menu(options))
        license = input(cli_prompt) #TODO: Validate
        print('Lets review your input.\n')
        print('  Name: {}'.format(name))
        print('  Description: {}'.format(description))
        print('  License: {}'.format(options[int(license)]))
        print('Is everything correct? (yes, no)')
        ok = input(cli_prompt).lower()
        if ok == 'yes' or ok == 'y':
            correct = True
            git.make_project(name, description, license)
            print('Great, visit your github profile https://www.github.com/')
        else:
            print('Woops, lets go over the information again!')


def options_menu(options):
    """Creates string representation of the licenses support by gitpal.

    Args:
        options: A dictionary of numbers to license name

    Returns:
        A string showing the options menu
    """
    buf = []
    for key, value in options.items():
        buf.append('  {}. {}\n'.format(key, value))
    return ''.join(buf)


def main():
    prompt(banner(), LICENSES)


if __name__ == '__main__':
    main()

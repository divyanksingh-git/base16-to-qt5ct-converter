import glob

base_dir = "base16-schemes/"
generated_dir = "qt-base16-generated/"

theme_list = glob.glob(f'{base_dir}*')
theme_list = list(map(lambda x:x.replace(base_dir,''),theme_list))

def converter(scheme,author,base00,base01,base02,base03,base04,base05,base06,base07,base08,base09,base0A,base0B,base0C,base0D,base0E,base0F):
    return f'''/*
*
* Base16 {scheme}
* Author: {author}
*
*/

[ColorScheme]
active_colors=#ff{base0C}, #ff{base01}, #ff{base01}, #ff{base05}, #ff{base03}, #ff{base04}, #ff{base0E}, #ff{base06}, #ff{base05}, #ff{base01}, #ff{base00}, #ff{base03}, #ff{base02}, #ff{base0E}, #ff{base09}, #ff{base08}, #ff{base02}, #ff{base05}, #ff{base01}, #ff{base0E}, #8f{base0E}
disabled_colors=#ff{base0F}, #ff{base01}, #ff{base01}, #ff{base05}, #ff{base03}, #ff{base04}, #ff{base0F}, #ff{base0F}, #ff{base0F}, #ff{base01}, #ff{base00}, #ff{base03}, #ff{base02}, #ff{base0E}, #ff{base09}, #ff{base08}, #ff{base02}, #ff{base05}, #ff{base01}, #ff{base0F}, #8f{base0F}
inactive_colors=#ff{base0C}, #ff{base01}, #ff{base01}, #ff{base05}, #ff{base03}, #ff{base04}, #ff{base0E}, #ff{base06}, #ff{base05}, #ff{base01}, #ff{base00}, #ff{base03}, #ff{base02}, #ff{base0E}, #ff{base09}, #ff{base08}, #ff{base02}, #ff{base05}, #ff{base01}, #ff{base0E}, #8f{base0E}
'''
for i in theme_list:
    with open(f'{base_dir}/{i}') as file:
        args = [];
        for line in file:
            if line[0] == '#':
                continue
            line = line.replace('\n','').split(" ")
            if len(line) < 2:
                continue
            args.append(line[1].replace('"',''));
        
        converted = converter(*args)
    
        with open(f'{generated_dir}base16-qtct-{i.replace('.yaml','')}.conf','wt') as conv:
            conv.write(converted)
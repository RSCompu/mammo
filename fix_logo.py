import base64
import os

html_path = 'invoice.html'
logo_path = 'logo.png'

print("Reading logo...")
with open(logo_path, 'rb') as f:
    logo_data = f.read()
    logo_b64 = base64.b64encode(logo_data).decode('utf-8')
    data_uri = f"data:image/png;base64,{logo_b64}"

print("Reading HTML...")
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Target string to replace
# We look for the exact line present in the file now
# Based on view_file output lines 461-462:
# <!-- Embedded Base64 Image to fix PDF Tainted Canvas issues -->
# <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAABkCAYAAADDhn8LAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAABbfSURBVHhe7Z0JcFTVnsf/t7Mv6Wx0NklIwiYkLAmEkLAJCLKJCMiOG6M4+pxXfTqjjqPPd6bK0XF8j6+cV2fmvTqOA4Iii4AisgqyCAQIG0tYwpo9nU6Szn7v3O6+t7vTSSch6fT9flW30u/e+7/33vP/n3Puvu92z+0o57TXPkUkaY+VI1Isjw+K2Ls5lurJp0iRUoqIo3ITKV+ROuVRwGNkgoCSXFHC+9ovUMYXZBFfWYXGZi2tOx1rZ/nYOTbyV61f3EUjow+PfP7+Fya2bXvzSBiex7I64QUCPQLyF9/bwA8QGBYC0zMzyaFr1+bkE/Kfm5x8tTo1uTco1/7CFYuPGi94SavgfIfy+dluyGWj0F1r85jXrBO+764VG7rnU84zea9Y5BkmL5TzFDJnEeeLPJ45KhGp3n8e/yQ2HMWA1MqUt0mOsRxraZuWX4oNbnhnxUY/W9JeCD7WT3mz9/b4YE8cV+oPuEBPvB+skJinx2f0Liijz5FU9kWc3Xtz9mdSJx3hHMnPyZGk8lPuV3N27y11S7GVkgOyL+VF/X2pS/bF3JXySAlLMW7mqahApApEvKCXOs5zvG+5HI8TxdwvzeUtG7ljJRyoGSfxXBy356L4svGLB5ou32OKxYdrW7d+fXyyvv9UFL0n4y9PFSO8QAAElgl4y1vYAIEhJCD3So/Mz1852W2+H0xNvT4+ufU5vzr2sPVKz6bk/azh9Eft3DXC3HYjm0ddm9uYZ+2RNtTVmohnf5jzzJD4nrpI8XbOhiNGlLPpiDmkPI5vfmRS/qQqNiGVe0SsnPN2hYCkFDnel3ySlKW4jKi/30+lrGwrcrSXx9sieT+Xz9s9O+L78yRx5Jd8HiMR2yO3hPievWfqkjze+lSK9xSf53F8j1PidEl9syZ+ZbyTeY40p/aGuGN83z7nWc+cbx30Rb3zuUgvVfTpS7alBsW1SF9zxznb7x5HNnBiw3ZeATnmalXAKyQ+ZbnPS+1EkYwFz8a7xiUL3bg1G3fnGs5dsJ7341Kl8pd5ufDEDz300KsTSXJcHiMst2AIrxAAgVsS8G6Zi0wQGEICvCQfHZn/5MqfhounR+uj+6r12u6RcmU7FQrPGPJ+EpM7F9rs6qLJ2otZErXS1LSzNOXleeswLy7mkvA9W74/Tyn337JdGjYgy8bubiC+J997y3aW35bUeB4vnbOkHG/nXC5nPyM2Nw7B79X9iYlRcuHeW853vS2inNOVsrwvx/qpufFvFJG9SY73pSwXoX4qsWR/ZSr1iXr5fEBm2rItUrwvkm2RxJSUswdtU2zWOhvV41RkSC0ZNvc/zRUJz4hXRyKt/fG9cGozaZeRyZg/3xqxYZjp2bZJP04oP+B5hec/y5UdqlZ7Nhodff1Mp/N/vCLTlOd8S70QCIDAHyawuv/b/OHzcQQE1h0BeWjN6UajdbLVuph+8QsHC5XKy9XxsaeKIrUve37xcTa37/Dc/H/YQM60nbvcdHZ+0Zp2w+q4YbOkZTNa43kGT5bv6+YkD3WJ+S9F0sz3KGPjllQHPk9tPjJs4sZTZDkV5eSx2S2JZKbK+3STpIyA6xmj4oVvVn+GLKnh+jKRT7T0nXSilLeXxW1IuC2Rr6gbKIo5FSXcji4ypbh9RBLL8Cxc5Phm97I4T3FLuWoScXXEYYhDkGyLem1URI4LyNP1JBVZPmi4Da5YIFcokPwrzDrmIXVHXhORIxHzpKZN25qRbtg0aiaaTdZ11ybrtsl0+7b9O3U71yQzZ2Gu39z/44fkrwzVx3ZNjFX2pUn3oHwQ8tzcXOuX6z8hFggMIwH+szyM44Y2g8BtEDh37lz2frPZPN5szpyO2yfd1MT+Sq32neL4+K5Crf4lk4Rfsr7/mCbv+Zjops5u57TQPQ+01+3cMtpqTcSzaTczUnFGZDKyObkHb5VPjs3MsmEadr8lcQHet2x+uneMlgyf/8LsstET26cnInI38mzvuOwrLi/nSMqSfJZhcbxZmvPqMhxtpSS/v59RuX58aZfIccxlcVuJ28HdIlEvn39ZpIxZ7he3RSm+KGBxqjlfZDiKLOcyd2zkOdvZ8PK6ZqVcJuHiSa66bGlKukStLmWrslRmpid++0F5u23gf9kVgl3FycnXFycqPx43yWG5AJtuNpt4tjoPgqE34kAEbv0E+M/yrc+BeACBu04gmZ+fdh6Zn3/lZLf5fjA19fr45Nbn/OrYw9YrPZuS97OG0x+1c9cIc9uNbO5xbW5jnrVH2lBXayKeHeY8IyS+py5SvJ2z4YgR5Ww6Yk4ij+ebH5mUP6mKTUjlHhEr57xdISApiRz5JZ8kZYnLiPr7/VTKyrYiR3t5vC2S93P5vN2zI74/TxJHyqHndZLE9shtF19JHu99KsV7is/zOL7HKXG6pL5ZE78y3sk8R5pTe0PcMb5vn/Osu8751kFf1Du/H+mlij59ybbUoLgW6WvunLN73ePIBk5s2M4rIMdcrQp4hcSnLPd5qZ0okrHg2XjXuGShG7dm4+5cw7kL1vN+XKpU/jIvF574oYceeXUiSY7L44RlFwzhBQJ3g4C3vIUNEOgLAXlIPjoy/8mVnxYWLxyrj+yr1Wu7R8qV7VQoPGO4/0lM7lzosquLJmsvZknUSlPTztKUl+epw4t5JHzPlu/PU8r9t2yXfmy4A8iysbsbiO/J996yneW3JTWex0vnLCnH2zmXy9nPiM2NQ/B7dX9iYpRc6HzL+a73RZRzulKW9+VYPzU3/o0isjfJ8b6U5SLUTyWW7K9MpT5RL58PyExbtkWK90WyLZKY0pJz13XORu04FRlSS4bN3U9zRcIz7NWRSDvd9r1wajNpl5HJmD/fGrFhmOnZtkk/Tig/4HmF5z/LlR2qVns2Gh19/Uyn83+8ItOU53xLvRAIgIDcCDY3AoF1RODcuXPZ+81m83izOXM6bp90UxP7K7Xad4rj47sKtfqXzIT/kvX9xzR5z8dEN3V2O6eF7nm/f7p2bjlt9SYir5Xpp1nSCSPSMmxu68Hj5ZNjM21Z9rV3HjA80C2hFw+2P5U+RksG22/33bLR0/VTYxG5G3n2zG37isvLOZKype96zJqD9W2lJL+vv1GZp9/rEjmOuSxuK3E7uFsk6uXzL4uUYcv94rYoxRcFLM7i5osMR5HlXNY5G3nOdTbyFmY1WyiTcPEkV13WNCVdolaXrFSZqY6Ov5+Qt3P+S/7Lzh3ZXZ6cen1xYuLHiSY5LBdg081mE89W50HAGwRugwD/Wd7GWTgFBIaTgJOH15wIwwU2+ZnTrdaZqQcfPDhar/90Ymryn+tTE08XqtXtbNZPJkQvpqTe6mh7MdTpXFNnrVBn7TBLu90s6XTeQ5JJZpvL2qNZZHmm+oF5T12jQ2JS+h6/V5yTZlbfk9Qcz6qN75Ni48vpfr2YvWGD1HycpWL77fVEfNGgvIBcrnriveve95T3cpo7cs6RR+466M+KlKO+cjfnEiZ1pZ8k34W3ishxfZJqP6t7huwXybGsV+CZ9oPzgoBXu15PMrPWpQIZnombyG0h6OzzKOM2+r4XOyEtRqE0w24WpkkU6iQMTRrKsp0NXfaxVf4wm/pLd+TvKddqT1br9b994KGHXt6+ffu31/XgL7wQCAyOAB6OD44tIm8lAem6u/76+fkrJ7vN94OpqdfHJ7d+/9dTH7be6NmMvJ82nP2onbtEmNtut/OoZ3Mb1z12Wxvqao/Ho8OcZ5Ykt6culFw7b7t8RDmbvjgjkdP0TUpE9iSl7AlVXEJq30F55Vy4KwQkpdCRX/KJUu7fMrLu3++l0t+2Ikd7eTy96b6fbx6W2z3T4vvzJHHkl3weIxHbI7e+dM/ednlJHm99KsV7is/zOL7HKXG6pL5ZE48y1sk9R5pZe0PcMb5vn/OsZ8637vmK3nnfRy9V9OlLtqUGxbVIX3PtHPZ7xxE2cELP23kFcszVqoBXSHzKcp+X2okiGQue5dfGJZ9049Rs7J5r+Hah4bwfk5qVv8zL5cd+6KGHE02SHJe3iG3r923wAgEQGAwBeM0ZDFdE3VoC8uT7aHf2+ivH5+ePNhpnkk7HyPj43snJbY/71bGHrFfOp+TS19u5R61386hhc/cId68y3p0h6e30V4ZJeU9dKP2dM5L5COeZEem79E1KnE+qwhNS9wzIq/WCu0JAUgpd9EteSUpUXIZVv9+XMn9TkaO9PM4WybvVfH3WfXfk+/MkceSXfB4jEdstt8X0nn2gI8njrU+leE/xeR7H9zglyo4v4ldK2ZlnSXO4N5R3jO/b5zzrmfOtfd6od9700kSV9OlLtqUGxbXIXnPXOX+r9zmygROv2c4rkGOuVgW8QuJTlvu81E4UyVg45d2FbrIwyXbm7W7xO/5X5XL5b/Jy4fEfPHTfbybL5bjkXG8W244//rMJeYHADREoFAoGvjEcwQ0QGHMCMn/RkflPrvxpuHhitD66r1qv7R4pV7ZTofCMIe8nMblzoc2uLpqsvZglUStNTTtLU16epw4v5pHwPVu+Px8l5b4t3bX3Y1YpNgDLxu5uIL4n33vLdpbfllQf4Xvp7M+U4+1cyuXkZ4TMjUPwsbr/Qx+Vcw/ccn7obRHlnK6U5X051k/NjX+jkNqT5HhfinK+6qcSS/ZXplKfqJfPB2SmLdsixfsi2RZJTEk5e9A2xWat7WzUjlORbT4ZNvc/zRUJz4hXRyKt/fG9cGozaZeRyZg/3xqxYZjp2bZJP04oP+B5hec/y5UdqlZ7Nhodff1Mp/N/vCLTlOdxSz2+c04Dlz5n9z/nNPDQ0wARCAymAYaeBg7mDCI6CAyuAd4scZ33vP/8+fN75uevHO003w+npl6b2Lbd/0p9x7c/27Jt2w+a99z9L5K4779KGP5xTttXclp+U+bXvE4v9UZkXo082725k3q7O7lvvJ09JvNqXqccb+d88RSRL/KcJ7W82KSS8gVS/hFSniF1bFLq3kXKi+e9XTHlaChyvK+4rKTc3xJRH98XKcOVJd4SKe9Lec3n2fW12H3fny9d/yUf8xiJ2T65peU9e0eP5PHWq1K8m3y+L3Z8j1Pi9Epdj039Cnk7i2R0n3y3aT1HuiZ1d4+4Z/yCfc675vP2Q3+0/qDno+9U+em/ZltqzNyL9DV3g3N8Xj5HNuT7t/MK5Jmr5X3e4/iU5T4rtRN5Mgqc8e8a93jSzXuzcXOu4dyJ+vn3JyuVX8+X81++7/4H/m4ySY7J48iWj289DSBQFAoFA5c+vVv/v6s0QP5dM4G5+e5wbdv41ESt+XitWn2qVCq9WBoZeaYwUvuy5xUf5yS37wjcvP+gIf9n7dy3bXZ90eamG9k86tqsZW3WEu62GuLZbubtJsm2UxeS4u2cDZv98TzJ2XTEnEQeI1Mfl0Q6qfI9UoFfROTsAVdcQkpS5HhfKUtSxpeV+vv8tFDKsh/laM/H2yJ5P6evfH29P98XS16S5/OYYrZPbnnpnr2jT+rx1q/YeE/xeR7H9zgtTv12oQ/KWBfjHGuO7Q2LZ/yCfR3o95z77Xf90W/6PtZNE/v0JdtSg+JapK+5c53D844jGzjx9dt5BeSYq+V8PiDxKct9XmonsmQsOBvfNe7RpJu3Z+OuXON4E83zPyqXKr8tlwtP3nPffT+bTJLj8jjBtx60wQsEBoEAXvYOgiii7ioB75Z58vDaM3MzM8kLZw92m++H09NvjE1te+6Xr9Z2Wm/0ZLLwWcvpj9u5h4S5w27nYdfmNj26I9KGU62JeDab89SE1Pe0xZ7tnA3rEZ5n0xHTE3k836Q8LIlkUhX+Eak1HxErz3u7Ig1JUY73lSwnKV9R6u/3U74k24oc7eV4WyTv5/J5u2dH/P48iRzpJc/3GCk22yO3fOmevaNH8njrVSneUzyex/E9TonzJXW9NnGlvJ15jjSn94bFM37Bvub1nHPuQ3+0/qDno+9U+em/ZFtqUNyL9DV3vvN2v3wc2ZAT37CdVyDPXC3v8wGJT1nu81I7kSdjwdn4rnHPk27em427cw3nTlTP/6hUKv+2XC48ecc99/xoMkn2y+OIZS9s/f1fT019kI8f/v5bX796tXnNlVde+cK1xou4QQAEVk8AD8erZ4WSe0zgkksuSc8+9dRofWzP2NjE9s+Vq7Xny6PjzwT+yJclv/hYThof51b+MWHu2/m779o0sveb0fj0zW6r9YQZan/f061Hw2jr03a49R2Zbn4j0/P/zIymX7d3+J7p9m+Znr/b9Hy5z+86Pd9TmeH37B2eZ4aT37LDyZ9k7vDr7HDz/7J72s+x1ub323Tzm2xo+4/M0Pa37HD9a26h9uX89jv+rLjrroP3T00t3l6rjRyqVqvvjJTLR8vF4onR8bGzlaGhy1zHOSu4+y+877xzc3cMDxFBYGgIyD2R+79QKIx8+4UXXtq2fesPd0+M/49yofhU0CvuywX5R3LS/Lid20eEuW/zcvuIyO8jKudtIqXn6yMl5U31fJGSdE5FKa2j5KsiZb6i2FcUxXqK1Zei9JS+16eifp5F32f91Fv6Xh/93/eI0v682C+KIvV54vR9n7c+lOJ9xed5HN/jNE33J66+KGOd3HOkmb03LJ7xC/Z1oN9z7rff9Ue/6ftYN03s05dsSw2Ka5G+5s51Ds87jmzgxNdv5xXIMVfL+3xA4lOW+7zUTmTJWHB2vWvc70k3/+76XXccazSbj9brJ07Va2eOTU6d2TY+fvJ7O3e+/vWvf/2C67rLGIZ/N3/55V39P6L9m7/5m3O53G9267/k1G63l6anp9V99923i6+1RKS6mQTM6dOn93zyyad7t23dcmisVttdGhnZlQuC/QEvP+oGgbyIuEKY80WpL4g0IEqZI2J9U6SCiGKKfVOk2DfF4j6i7/VpQB9RX/S4Pu+L3/c9Xj7PE6fv+7z1oRTvi9/nZ5/HaZrmT1x9UU4pmeNI03tveH7Pz/vXhXbP9W56vTf1Jvo+1k0T+/Sl21KD4hK9a+70Xee1fBxv6MRnLe8VeObK+/x5iU3Z3rN+O5EnY8HZdde4n5MuD/V7n+5Vj3+W00LDeYV10J0zPq+VSsWj4+PjJ+v1k3vGx06cvu+++158+umnX3Rdt4Zh+D/wL/FCIFAoCgV1z+S/5+c/3TVUH9u/o77l4GSttnN8bOxwZWzsj3m/8EjecfbktPFhO/ddme8iYe47otx3RP57RCrnPSKl571P5LyfiPLy3idSXi7lRSnlfSJlvaIo01Okvvc9orS/WNIv4vR83/d560Mp3ld8nsfxPU7TfH/i6osy1sk9R5rZewM84xfs60C/59xvXxeN5u9j3TSxT1+yLTUorkX6mmvnsN87jmzgxG+38wrkmasVeIXEpyz3eakdeZJ3F2TZuEu6S23/B7/9w9//7ne/+4eXFxeP1+v1/WNjYyf2TE6+XqvVXqlWq88Wh4fvLgSB/J/n8qNu0P2P/P/1c+f+H5A2tJ+vF2R2AAAAAElFTkSuQmCC"
#
# But wait, looking at the view_file output, the line is heavily truncated in the tool output too!
# It ends with '...' or similar if it's too long in tool outputs.
# Wait, actually view_file result in Step 160 shows a HUGE base64 string on line 462.
# "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAABkCAYAAADDhn8LAAAAAXNSR0IArs4c6QAAAARnQU1..."
# And it ends with "5/n3Puvu92z+0o57TXPkUkaY+VI1Isjw+K2Ls5lurJp0iRUoqIo3ITKV+..."
# It looks like the file actually CONTAINS that truncated text if the tool just wrote what I gave it.
# The previous replace_file_content MIGHT have written the truncation markers literals if I wasn't careful?
# NO, wait. I provided "..." in the ReplacementContent in Step 142? No, I provided the full string in Step 142 tool call.
# BUT, the tool output logic might have truncated *display* but written fully.
# HOWEVER, the file content view in Step 160 shows the line is suspiciously similar to what I see in the logs.
#
# REGARDLESS of what is in there now, I want to replace the whole <img> tag with a fresh, correct one.
# So I will find the lines surrounding the img tag and replace them.

start_marker = '<div class="brand-section">'
end_marker = '<div class="shop-info">'

try:
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    if start_idx != -1 and end_idx != -1:
        # Construct new content
        new_img_tag = f'\n                <!-- Embedded Base64 Image -->\n                <img src="{data_uri}" alt="Logo" class="logo-img" onerror="this.style.display=\'none\'">\n                '
        
        # We need to preserve everything before start_marker + len, and after end_marker
        # actually, the structure is:
        # <div class="brand-section">
        #    ... img tag ...
        #    <div class="shop-info">
        
        # So I will replace everything between brand-section start and shop-info start.
        
        pre = content[:start_idx + len(start_marker)]
        post = content[end_idx:]
        
        new_content = pre + new_img_tag + post
        
        print("Writing updated HTML...")
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Success!")
    else:
        print("Could not find markers.")

except Exception as e:
    print(f"Error: {e}")

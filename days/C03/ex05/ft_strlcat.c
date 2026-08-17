/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sboukhel <sboukhel@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/17 12:58:23 by sboukhel          #+#    #+#             */
/*   Updated: 2026/08/17 21:28:11 by sboukhel         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	strlcat(char *dest, char *src, unsigned int size)
{
	unsigned int	i;
	unsigned int	j;

	i = 0;
	j = 0;
	while (dest[i] != '\0')
	{
		i++;
	}
	while (src[j] != '\0')
	{
		if (i + j + 1 < size)
		{
			dest[i + j] = src[j];
		}
		j++;
	}
	if (i < size)
		dest[i + j] = '\0';
	return (i + j);
}
